from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic.edit import FormView
from .models import Computer,ComputerBrand, ComputerSpecification
from .forms import CreateModel,ComputerSpecificationFormModel,ComputerBrandFormModel
from django.http import JsonResponse
import uuid
import base64





# class based view for lists of computers
class ComputerList(View):
    def get(self, request):
        computer_listing = Computer.objects.all()
        return render(request,'computer/homepage.html',{'Computerlist':computer_listing})



# class based view for creation of computer information
class ComputerCreate(FormView):
    model = Computer
    form_class = CreateModel

    def get(self,request):
        brandname =ComputerBrand.objects.all()
        computer_specification = ComputerSpecification.objects.all()
        form = CreateModel
        return render(request,"computer/add_computer.html",{'form':form,'brandname':brandname,'computer_specification':computer_specification})

    def post(self,request):
        try:
            brandname =ComputerBrand.objects.all()
            computer_specification = ComputerSpecification.objects.all()
            form = CreateModel(request.POST)
            
           
            # for i in totalimage:
            #     print(i)

            if form.is_valid():
                form_data = form.cleaned_data
                computer_code = form_data.get('computer_code')
                computer = form.cleaned_data.get('computer')
                quantity = form_data.get('quantity')
                unit_rate = form_data.get('unit_rate')
                computer = Computer.objects.create(computer_code=computer_code, computer = computer, quantity=quantity, unit_rate=unit_rate)

                totalimage = self.request.POST.get("totalimage")
                print(totalimage)
                for image_sn in range(0, int(totalimage)):
                    print(image_sn)
                    image =  self.request.POST.get(str(image_sn))
                    print(f"input Image: {image}")
                #  save to media/computer/computer.id/   

                
                # if totalimage:
                #     image_parts = image_data.split(";base64,")
                #     image_type_aux = image_parts[0].split("image/")
                #     image_type = image_type_aux[1]
                #     image_base64 = image_parts[1]
                #     image_data = base64.b64decode(image_base64)
                #     print(image_data)
                #     file_name = f'static/webcam/{uuid.uuid4()}.{image_type}'
                #     with open(file_name, 'wb') as f:
                #         f.write(image_data)
                    
                

                
                return redirect('dashboard')
            return render(request,"computer/add_computer.html",{'form': form,'brandname':brandname,'computer_specification':computer_specification})
        except Exception as e:
            print(e, 9090)
            return render(request,"computer/add_computer.html",{'form': form,'brandname':brandname,'computer_specification':computer_specification})

    
    



# class based view for thank you page
class Thanks(View):
    def get(self, request):
    
        return render(request,'computer/thankyoupage.html')


# class based view for detailing of computer information
class ComputerDetail(View):
    def get(self, request, id):
        Computerdetail = Computer.objects.get(id=id)
        return render(request, 'computer/homepage.html', {'detail':Computerdetail})


#class based delete operation 
class ComputerDelete(View):
    def get(self, request, id):
        Computerdelete = Computer.objects.get(id=id)
        Computerdelete.delete()
        return redirect('computerlist') 




# class based view to update computer information
class ComputerInfoUpdate(View):
    def get(self, request,id):
        brandname =ComputerSpecification.objects.all()
        update = Computer.objects.get(id=id)
        computerupdate=CreateModel(instance=update)  
        return render(request,'computer/updatecomputer_info.html',{'updatecomputerinfo':computerupdate,'brandname':brandname})

    def post(self,request,id):
        brandname =ComputerSpecification.objects.all()
        update = Computer.objects.get(pk=id)
        computerupdate = CreateModel(request.POST,instance=update)
        print(computerupdate)
        if computerupdate.is_valid():
            print("valid")
            computerupdate.save()
            return redirect('computerlist')
        print("invalid")
        return render(request,'computer/updatecomputer_info.html',{'updatecomputerinfo':computerupdate,'brandname':brandname})







# view for computerspecificationform
class ComputerSpecificationView(FormView):
    model = ComputerSpecification
    form_class = ComputerSpecificationFormModel


    def get(self,request): 
        form = ComputerSpecificationFormModel
        print("get request ")
        return render(request,"computer/computerspecificationform.html",{'form':form})


    def post(self,request):
        try:
            form = ComputerSpecificationFormModel(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                brand = form_data.get('brand')
                generation = form.cleaned_data.get('generation')
                price_min = form_data.get('price_min')
                price_max = form_data.get('price_max')
                ram = form_data.get('ram')
                add = ComputerSpecification.objects.create(brand=brand, generation=generation, price_min = price_min,price_max=price_max, ram=ram)
                return redirect('/usersettings/')
            return render(request,"computer/computerspecificationform.html",{'form': form})
        except Exception as e:
            print(e, 999999999)
            return render(request,"computer/computerspecificationform.html",{'form': form})



# view for computer brand form
class ComputerBrandView(FormView):
    model = ComputerBrand
    form_class =ComputerBrandFormModel


    def get(self,request): 
        form = ComputerBrandFormModel
        print("get request ")
        return render(request,"computer/computerbrandform.html",{'form':form})


    def post(self,request):
        try:
            form = ComputerBrandFormModel(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/usersettings/')
            return render(request,"computer/computerbrandform.html",{'form': form})
        except Exception as e:
            print(e, 999999999)
            return render(request,"computer/computerbrandform.html",{'form': form})



# view for computer specification field (add computer button)
class ComputerSpecification_Opt(View):
    def post(self,request):
        id = request.POST.get("id")
        print(id)
        # computer_brand = ComputerBrand.objects.get(id=id)
        computer_specification = ComputerSpecification.objects.filter(brand=id)
        computer_specifications = list()
        for i in computer_specification:
            computerspecification_data = {}
            computerspecification_data['id'] = i.id
            computerspecification_data['ram'] = i.ram
            computerspecification_data['generation'] = i.generation
            computer_specifications.append(computerspecification_data)
        return JsonResponse({"data": computer_specifications}, status=200)








class upload_image(View):
    def post(self,request):
        image_data = request.POST.get('image')
        print(image_data)
        # Check if the image data exists
        if image_data:
            # Split the image data to get the image type and base64 encoded image
            image_parts = image_data.split(";base64,")
            image_type_aux = image_parts[0].split("image/")
            image_type = image_type_aux[1]
            image_base64 = image_parts[1]

            # Decoding the base64 encoded image
            image_data = base64.b64decode(image_base64)
            print(image_data)

            # Generating a unique filename
            file_name = f'static/webcam_images/{uuid.uuid4()}.{image_type}'

            # Save the image to the specified folder
            with open(file_name, 'wb') as f:
                f.write(image_data)
        return render(request,'computer/capture-photo-with-webcam.html',{'image_data':image_data})



