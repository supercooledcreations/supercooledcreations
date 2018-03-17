# Import
# Django
from django.contrib.auth import get_user_model
from django.db import models

DETAIL_RECORD_TYPES = (
    ('boolean', "True/False"),
    ('integer', "Count"),
    ('float', "Value"),
    ('duration', "Duration of Time"),
    ('character', "Short Description")
)


# Models
# Base Metric
class BaseMetric(models.Model): # TO DO ADD SLUG FIELD AS ID
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# Detail Metrics
class DetailMetric(models.Model):
    name = models.CharField(max_length=128)
    base_metric = models.ForeignKey(BaseMetric, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=16, choices=DETAIL_RECORD_TYPES)

    def __str__(self):
        return self.name


# Base Record
class BaseRecord(models.Model):
    timestamp = models.DateTimeField()
    base_metric = models.ForeignKey(BaseMetric, on_delete=models.CASCADE, limit_choices_to={'record_type': 'base_record'})


# Detail Records
class DetailRecord(models.Model):
    base_record = models.ForeignKey(BaseRecord, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BooleanRecord(DetailRecord):

    detail_metric = models.ForeignKey(DetailMetric, on_delete=models.CASCADE, limit_choices_to={'record_type': 'boolean'})
    value = models.BooleanField()


class IntegerRecord(DetailRecord):

    detail_metric = models.ForeignKey(DetailMetric, on_delete=models.CASCADE, limit_choices_to={'record_type': 'integer'})
    value = models.IntegerField()


class FloatRecord(DetailRecord):

    detail_metric = models.ForeignKey(DetailMetric, on_delete=models.CASCADE, limit_choices_to={'record_type': 'float'})
    value = models.FloatField()


class DurationRecord(DetailRecord):

    detail_metric = models.ForeignKey(DetailMetric, on_delete=models.CASCADE, limit_choices_to={'record_type': 'duration'})
    value = models.DurationField()


class CharacterRecord(DetailRecord):

    detail_metric = models.ForeignKey(DetailMetric, on_delete=models.CASCADE, limit_choices_to={'record_type': 'character'})
    value = models.CharField(max_length=128)
