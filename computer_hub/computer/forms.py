from .models import Computer,ComputerSpecification,ComputerBrand
from django import forms

# form for computer information
class CreateModel(forms.ModelForm):

    class Meta:
        model=Computer
        fields=['computer_code', 'computer','quantity','unit_rate']
        widgets = {
            'computer_code':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            'computer':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            'quantity':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            'unit_rate':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
         }
        labels = {
        'computer': "Computer Brand"
        }


    def cleaned_computer(self):
        computer = self.cleaned_data['computer']
        try:
            computer_spe = ComputerSpecification.objects.get(computer=computer)
            # ComputerSpecification.objects.values_list('computer').distinct()
            # computer_spe.value_list('computer').distinct()

        except Exception as e:
            raise e



# computer specification form
class ComputerSpecificationFormModel(forms.ModelForm):
    class Meta:
        model = ComputerSpecification
        fields=['generation', 'price_min','price_max','ram','brand']
        widgets = {
        
            'brand':forms.Select(attrs={'class':' form-select form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            'price_max':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            'generation':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            'ram':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            'price_min':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
         }
        labels = {
        'brand': "Computer Brand"
        }


# computer brand form
class ComputerBrandFormModel(forms.ModelForm):
    class Meta:
        model = ComputerBrand
        fields=['brand_name' , 'logo']
        widgets = {
            'brand_name':forms.TextInput(attrs={'class':' form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            # 'logo':forms.ImageField(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
           
         }