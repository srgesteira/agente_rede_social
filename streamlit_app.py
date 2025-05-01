import streamlit as st
import dropbox

st.title("Agente de Rede Social - SrGesteira")

# Token de acesso direto ao Dropbox
DROPBOX_TOKEN = "sl.u.AFsg7vRjR9AvolulF9YtCd2IU5jt4AIhgDDDJQq2EWIPdtPIEPWBKUk_9-9DKTeBXZ0I6iZORpEDJB87bI_a-SDQcY69AZC-a-AZC-ox4Lv3VRU8DpsJhEocJhEocFHP6bcMYSWIGNayn4v4v4v4v4v5PH5PH5ERYt794lL_T8fB8fB8XN1BqU65eBsinv0BjJJJJ_3uYeo13jli7PU3eJU1gOhxg3eJ_3eoJ3eJ3eJ"

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
