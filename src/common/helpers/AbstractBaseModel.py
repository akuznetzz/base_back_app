from common.mixins.TimestampMixin import TimestampMixin


class AbstractBaseModel(TimestampMixin):
    class Meta(TimestampMixin.Meta):
        abstract = True
