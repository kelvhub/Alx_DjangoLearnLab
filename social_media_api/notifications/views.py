from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user)
    data = [
        {
            "id": n.id,
            "actor": n.actor.username,
            "verb": n.verb,
            "target": str(n.target) if n.target else None,
            "timestamp": n.timestamp,
            "read": n.read,
        }
        for n in notifications
    ]
    return JsonResponse(data, safe=False)

@login_required
def mark_as_read(request, pk):
    try:
        notification = Notification.objects.get(id=pk, recipient=request.user)
        notification.read = True
        notification.save()
        return JsonResponse({"status": "read"})
    except Notification.DoesNotExist:
        return JsonResponse({"error": "not_found"}, status=404)
