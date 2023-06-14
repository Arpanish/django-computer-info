from django.urls import path
from computer.views import ComputerList,ComputerCreate,ComputerDetail,ComputerDelete,ComputerInfoUpdate,Thanks,ComputerSpecificationView,ComputerBrandView,ComputerSpecification_Opt,upload_image
urlpatterns = [
    path('',ComputerList.as_view(),name='computerlist'),
    path('createlist/',ComputerCreate.as_view(),name='computercreate'),
    path('computerdetail/<int:id>',ComputerDetail.as_view(),name='computerdetail'),
    path('computerdelete/<int:id>', ComputerDelete.as_view(), name="computerdelete"),
    path('computerinfoupdate/<int:id>',ComputerInfoUpdate.as_view(),name='computerupdate'),
    path('thanks/',Thanks.as_view(),name='thanks'),
    path('computerspecificationform/',ComputerSpecificationView.as_view(),name="computerspecificationform"),
    path('computerbrandform/',ComputerBrandView.as_view(),name='computerbrandform'),
    path('computerspecificationopt/',ComputerSpecification_Opt.as_view(),name='ComputerSpecification_Opt'),
    path('img/',upload_image.as_view(),name='images'),
    # path('image',image.as_view(),name='image'),
]