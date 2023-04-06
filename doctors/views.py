from django.shortcuts import render, redirect

from doctors.api_istekleri import try_signing_in, try_signing_up


def home(request):
    if 'access_token' not in request.session:
        return redirect('sign_in')

    return render(request, 'doctors/home.html')

def sign_in(request):
    if 'access_token' in request.session:
        return redirect('home')

    error_message = ''

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        signing_in_request = try_signing_in(email, password)

        if signing_in_request.get('access_token'):
            request.session['access_token'] = signing_in_request['access_token']
            return redirect('home')
        else:
            error_message = signing_in_request['message']
            
    context = {
        'error_message': error_message
    }
    return render(request, 'doctors/sign_in.html', context)

def sign_up(request):
    error_message = ''
    if 'access_token' in request.session:
        return redirect('home')


    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        signing_up_request = try_signing_up(email, password)

        if signing_up_request.get('access_token'):
            request.session['access_token'] = signing_up_request['access_token']
            return redirect('home')
        else:
            error_message = signing_up_request['message']
            
    context = {
        'error_message': error_message
    }
    return render(request, 'doctors/sign_up.html', context)


def sign_out(request):
    del request.session['access_token']
    return redirect('sign_in')