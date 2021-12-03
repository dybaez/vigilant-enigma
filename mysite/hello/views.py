from django.shortcuts import render


# Create your views here.

def times_visited(request):
    sessionId = request.session.get('sessionId')
    if sessionId:
        if int(sessionId):
            sessionId = int(sessionId) + 1
    else:
        sessionId = 1
    request.session['sessionId'] = sessionId

    ctx = {'times_visited': sessionId}
    response = render(request, 'index.html', ctx)
    response.set_cookie('dj4e_cookie', '934ae3fe', max_age=1000)
    return response
