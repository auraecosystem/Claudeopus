import kagglehub

# Download latest version
path = kagglehub.model_download("web4app/claudeopus/transformers/default")

print("Path to model files:", path)
