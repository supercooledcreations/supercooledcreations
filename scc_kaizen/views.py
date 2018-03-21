# Import #
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.utils import timezone

# App
from .forms import (
    detail_records,
    BaseMetricForm,
    DetailMetricForm,
    RecordEntryForm,
)

from .models import (
    BaseMetric,
    DetailMetric,
    BaseRecord,
)


# Views #
# Metrics #
class BaseMetricListView(LoginRequiredMixin, View):

    # List
    def get(self, request, *args, **kwargs):

        template_name = 'scc_kaizen/metric_list.html'
        context = {
            'metric_list': BaseMetric.objects.filter(user=request.user).order_by('name'),
            'base_metric_form': BaseMetricForm()
        }

        return render(request, template_name, context)

    # Add base metric
    def post(self, request, *args, **kwargs):

        form = BaseMetricForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()

        return HttpResponseRedirect(reverse('scc_kaizen:metric_list'))


class BaseMetricDetailView(LoginRequiredMixin, View):

    # BaseMetric Detail, # DetailRecordList
    def get(self, request, *args, **kwargs):

        # Template Name
        template_name = 'scc_kaizen/metric_detail.html'

        # Context
        # Metric Detail
        base_metric = BaseMetric.objects.get(pk=self.kwargs['metric_pk'])
        detail_metrics = DetailMetric.objects.filter(base_metric=base_metric)

        # Edit this metric form
        base_metric_edit_form = BaseMetricForm(instance=base_metric)

        # Add detail metric form
        detail_metric_form = DetailMetricForm()

        # Record Entry Form
        record_entry_form = RecordEntryForm(initial={'timestamp': timezone.now()}, detail_metrics=detail_metrics)

        # Create record table
        # Table Header
        record_table_header = ['Timestamp']
        for detail_metric in detail_metrics:
            record_table_header.append(detail_metric.name)
        record_table_header.append('Remove')

        # Table Rows
        record_table_rows = []
        base_records = BaseRecord.objects.filter(base_metric=base_metric)

        # Grab and cache all detail records related to this base metric's detail metrics
        detail_record_qsets = {}

        for detail_record in detail_records.keys():

            detail_record_qsets[detail_record] = detail_records[detail_record]['model'].objects.filter(
                detail_metric__in=detail_metrics
            )

        for base_record in base_records:
            record_table_row = {'id': base_record.id, 'timestamp': base_record.timestamp, 'detail_values': []}
            for detail_metric in detail_metrics:
                detail_record_list = detail_record_qsets[detail_metric.record_type].filter(base_record=base_record, detail_metric=detail_metric)

                if detail_record_list.count() > 0:
                    detail_record_value = detail_record_list.first().value
                else:
                    detail_record_value = 'None'

                record_table_row['detail_values'].append(detail_record_value)

            record_table_rows.append(record_table_row)

        context = {
            'base_metric': base_metric,
            'base_metric_edit_form': base_metric_edit_form,
            'detail_metric_form': detail_metric_form,
            'record_entry_form': record_entry_form,
            'record_table_header': record_table_header,
            'record_table_rows': record_table_rows
        }

        return render(request, template_name, context)

    # Add Detail
    def post(self, request, *args, **kwargs):
        # Metric Detail
        base_metric = BaseMetric.objects.get(pk=self.kwargs['metric_pk'])
        metric_detail_redirect = HttpResponseRedirect(reverse('scc_kaizen:metric_detail', kwargs={'metric_pk': base_metric.pk}))

        # Edit Base Metric
        if request.POST['action'] == 'update_base_metric':
            form = BaseMetricForm(request.POST, instance=base_metric)
            if form.is_valid():
                form.save()
                return metric_detail_redirect

        # Add Detail to Base Metric
        elif request.POST['action'] == 'add_detail_metric':
            form = DetailMetricForm(request.POST)
            if form.is_valid():
                form.instance.base_metric = base_metric
                form.save()
                return metric_detail_redirect

        # Add Record to Base Metric
        elif request.POST['action'] == 'add_new_entry':
            detail_metrics = DetailMetric.objects.filter(base_metric=base_metric)
            form = RecordEntryForm(request.POST or None, detail_metrics=detail_metrics)
            if form.is_valid():
                base_record = BaseRecord.objects.create(
                    timestamp=form.cleaned_data['timestamp'],
                    base_metric=base_metric,
                )

                detail_entries = [{'detail_metric_id': x.split('_')[1], 'value': form.cleaned_data[x]} for x in form.cleaned_data if 'dm_' in x]

                for detail_entry in detail_entries:
                    detail_metric = DetailMetric.objects.get(id=detail_entry['detail_metric_id'])
                    detail_record_model = detail_records[detail_metric.record_type]['model']
                    detail_record_model.objects.create(
                        base_record=base_record,
                        detail_metric=detail_metric,
                        value=detail_entry['value']
                    )

            return metric_detail_redirect
        # Return 400 Error
        elif request.POST['action'] == 'remove_entry':
            entry_id = request.POST['entry_id']
            if entry_id:
                BaseRecord.objects.get(id=entry_id).delete()

            return metric_detail_redirect

        else:
            return HttpResponseBadRequest('Request Action not Recognized')





