def domain(request):
    scheme = 'https' if request.is_secure() else 'http'
    full_domain = f"{scheme}://{request.get_host()}"
    return {'current_domain': full_domain}
