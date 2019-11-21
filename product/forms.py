from django import forms
from .models import Product,City
  # City

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','title', 'description','price','condition','image','image_2','image_3','image_4','image_5','state','city','home_delivery','delivery_area','home_delivery_price','price_negotiable')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')