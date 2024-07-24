from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Report
from utils.aws_utils import upload_file_to_s3
import uuid
import os
from django.shortcuts import render




def report_form(request):
    return render(request, 'reports/submit.html')

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_report(request):
    if 'image' not in request.FILES:
        return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

    image = request.FILES['image']
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')

    if not latitude or not longitude:
        return Response({'error': 'Latitude and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)

    filename = f"reports/{uuid.uuid4()}{os.path.splitext(image.name)[1]}"
    image_url = upload_file_to_s3(image, filename)

    if not image_url:
        return Response({'error': 'Failed to upload image'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    report = Report.objects.create(
        user=request.user,
        latitude=latitude,
        longitude=longitude,
        image_url=image_url
    )

    return Response({'message': 'Report submitted successfully', 'report_id': report.id}, status=status.HTTP_201_CREATED)
    # return render(request, 'reports/api.html')