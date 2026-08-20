def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We dont have this flavor")
        else : print(f"{flavor} chai is served.")
    except ValueError as e:
        print("Error: ",e)

    finally:
        print("Next customer please!")


serve_chai("Masala")
serve_chai("unknown")