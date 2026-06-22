from decouple import config

CONFIG_DEBUG = config("DEBUG", cast=bool, default=True)
CONFIG_SECRET_KEY = config("SECRET_KEY")

# CONFIG_CORS_ALLOWED_ORIGINS = config(
#     "CORS_ALLOWED_ORIGINS",
#     cast=lambda v: [s.strip() for s in v.split(",")],
#     default=f"http://localhost:{config('NGINX_EXPOSE_PORT')}, http://localhost:{config('BACKEND_EXPOSE_PORT')},http://localhost:5173",
# )

# CONFIG_CORS_ALLOWED_ORIGINS = config(
#     "CORS_ALLOWED_ORIGINS", cast=lambda v: [i.strip() for i in v.split(",")], default=""
# )


CONFIG_CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS",
    cast=lambda v: [
        i.strip() for i in v.split(",") if i.strip()
    ],  # ← filter empty strings
    default="",
)
