from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subscriber, Suggestion


@api_view(['POST'])
def email(request):
    try:
        print("DATA:", request.data)
        print("POST:", request.POST)

        user_email = request.data.get('email') or request.POST.get('email')

        if not user_email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if Subscriber.objects.filter(email=user_email).exists():
            return Response({'error': 'This email is already subscribed.'}, status=status.HTTP_400_BAD_REQUEST)

        Subscriber.objects.create(email=user_email)

        return Response({'message': 'Email saved successfully'})

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SuggestionCreateView(APIView):
    def post(self, request):
        print("DATA:", request.data)
        print("POST:", request.POST)

        email = request.data.get('email') or request.POST.get('email')
        message = request.data.get('message') or request.POST.get('message')

        if not email or not message:
            return Response(
                {'error': 'Email and message are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            suggestion = Suggestion.objects.create(email=email, message=message)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({
            'success': True,
            'detail': 'Suggestion sent successfully.',
            'email': suggestion.email,
            'message': suggestion.message,
        }, status=status.HTTP_201_CREATED)
