def get_model_meta(view):
    return view.serializer_class.Meta.model._meta