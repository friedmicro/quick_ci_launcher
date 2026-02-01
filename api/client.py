def fetch_client(request):
    return request.args.get("is_client", "true").lower() == "true"
