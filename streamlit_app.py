import streamlit as st
import dropbox

st.title("Agente de Rede Social - SrGesteira")

# Token de acesso direto ao Dropbox
DROPBOX_TOKEN = "sl.u.AFu9mJv4P3KXUZ0P5onJ85edi1aknNBWx1aknNBWxUC_-RoM-qzOlJpulyj M0kFnLDxUQD6sI41dmk4jiGnPWhQ8TT00akTb9otcRdqQ4dt0t1Lea_oP6mHXZ-Ma7W7n8gUGSVrfz ICws4HOcq YBCBqhtC-obqJ7obqJ7oBU97MbcU9wIcjQz8ei7FZlu_36ji EUq6Tlk6Tlk6Ln-4AJTemBCj2CVpM8XKWfcKvpM8XKWfcK4qLRFcxm-TBUO-HWtdp81mat"

# Conectar ao Dropbox
try:
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    user = dbx.users_get_current_account()
    st.success(f"Conectado ao Dropbox como: {user.name.display_name}")
except Exception as e:
    st.error("Erro ao conectar no Dropbox")
    st.stop()

# Listar arquivos da pasta padrão do App Folder
st.subheader("Arquivos agendados na pasta do app")
try:
    result = dbx.files_list_folder("")
    for entry in result.entries:
        st.write("•", entry.name)
except:
    st.warning("Nenhum arquivo encontrado ou pasta ainda não existe.")

# Upload de arquivos
st.subheader("Enviar novo conteúdo")
uploaded_file = st.file_uploader("Escolha um arquivo para enviar (imagem, vídeo, PDF ou texto):")

if uploaded_file is not None:
    dropbox_path = f"/{uploaded_file.name}"  # salvará na raiz da pasta do App
    dbx.files_upload(uploaded_file.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    st.success(f"Arquivo enviado com sucesso para: {dropbox_path}")
