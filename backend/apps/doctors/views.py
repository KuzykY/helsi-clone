from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, UpdateAPIView

from core.permissions.user_permissions import IsStaff


from .models import DoctorModel
from .serializers import DoctorSerializer
from ..patients.serializers import PatientSerializer


class DoctorListCreateView(ListCreateAPIView):
    """
    get:
        Get all doctors
    post:
        Create doctor
    """
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()


class DoctorRetrieveDestroyView(RetrieveDestroyAPIView):
    """
    get:
        Get one doctor

    delete:
        Delete doctor
    """
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()


class AddPatientToDoctorView(UpdateAPIView):
    # serializer_class = AddPatientToDoctorSerializer
    serializer_class = PatientSerializer
    queryset = DoctorModel.objects.all()
    permission_classes = (IsStaff,)

    def perform_update(self, serializer):
        doctor = self.get_object()
        serializer.save(doctor=doctor)
    # def post(self, request, *args, **kwargs):
    #     doctor = get_object_or_404(queryset=self.request, pk=request.user.id)
    #     patient_id = self.request.data.get('patient')
    #     patient = get_object_or_404(queryset=PatientModel.objects.all(), id=patient_id)
    #     doctor.patients.add(patient)
    #     doctor.save()
    #     return Response({"detail": f'Patient - {patient.id} was added to a doctor {self.request.user}'})
