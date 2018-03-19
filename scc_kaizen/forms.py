# Imports
# Django
from django import forms
from django.utils import timezone

# App
from .models import BaseMetric, DetailMetric, BooleanRecord, IntegerRecord, FloatRecord, TimeRecord, DurationRecord, CharacterRecord


# Custom Fields
class EntryBooleanField(forms.BooleanField):

    def __init__(self, *args, **kwargs):
        super(EntryBooleanField, self).__init__(*args, **kwargs)
        self.required = False


class EntryDurationField(forms.DurationField):

    def __init__(self, *args, **kwargs):
        super(EntryDurationField, self).__init__(*args, **kwargs)
        self.initial = timezone.timedelta()

# Detail Record Models and Fields
detail_records = {

    'boolean': {'model': BooleanRecord, 'field': EntryBooleanField},
    'integer': {'model': IntegerRecord, 'field': forms.IntegerField},
    'float': {'model': FloatRecord, 'field': forms.FloatField},
    'time': {'model': TimeRecord, 'field': forms.TimeField},
    'duration': {'model': DurationRecord, 'field': EntryDurationField},
    'character': {'model': CharacterRecord, 'field': forms.CharField},
}


# Forms
# Metric Forms
class BaseMetricForm(forms.ModelForm):
    class Meta:
        model = BaseMetric
        fields = ['name']


class DetailMetricForm(forms.ModelForm):
    class Meta:
        model = DetailMetric
        fields = ['name', 'record_type']


class RecordEntryForm(forms.Form):
    timestamp = forms.DateTimeField()

    def __init__(self, *args, **kwargs):
        detail_metrics = kwargs.pop('detail_metrics')
        super(RecordEntryForm, self).__init__(*args, **kwargs)

        for detail_metric in detail_metrics:
            field_name = 'dm_{detail_metric_id}'.format(detail_metric_id=detail_metric.id)
            self.fields[field_name] = detail_records[detail_metric.record_type]['field'](label=detail_metric.name)
