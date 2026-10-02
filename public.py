from pyngrok import ngrok
import uvicorn
ngrok.set_auth_token("3K8czSWz0jPKMcVbyI3MVuv3JvX_2EGFWgugQKVyHRkbtEBxW")
# public link create pannuthu
public_url = ngrok.connect(8000)
print(f" * UN DEMO LINK: {public_url}")
print(f" * Idha teacher ku anuppu da!")

uvicorn.run("main:app", host="0.0.0.0", port=8000)