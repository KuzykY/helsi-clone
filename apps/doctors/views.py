from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response

from core.permissions.user_permissions import IsStaff

from ..patients.models import PatientModel
from .models import DoctorModel
from .serializers import AddPatientToDoctorSerializer, DoctorSerializer


class DoctorListCreateView(ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()


class DoctorRetrieveDestroyView(RetrieveDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()


class AddPatientToDoctorView(UpdateAPIView):
    serializer_class = AddPatientToDoctorSerializer
    queryset = DoctorModel.objects.all()
    permission_classes = (IsStaff,)

    def post(self, request, *args, **kwargs):
        doctor = get_object_or_404(queryset=self.request, pk=request.user.id)
        patient_id = self.request.data.get('patient')
        patient = get_object_or_404(queryset=PatientModel.objects.all(), id=patient_id)
        doctor.patients.add(patient)
        doctor.save()
        return Response({"detail": f'Patient - {patient.id} was added to a doctor {self.request.user}'})
