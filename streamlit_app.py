import streamlit as st
import dropbox

# Título do painel
st.title("Agente de Rede Social - SrGesteira")

# Token de acesso ao Dropbox (coloque o seu aqui!)
DROPBOX_TOKEN = "sl.u.AFuM2GuLTnClTliel2o9HNYsCLCcAtvD348dMHHvNWfrzfJRdU5AtG4TS4aKXPYgs1Cq4RBofxfy4hrNgGG"

# Conectando ao Dropbox
try:
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    user = dbx.users_get_current_account()
    st.success(f"Conectado ao Dropbox como: {user.name.display_name}")
except Exception as e:
    st.error("Erro ao conectar no Dropbox")
    st.stop()

# Listar arquivos da pasta /conteudos/agendados
st.subheader("Arquivos agendados")
try:
    result = dbx.files_list_folder("/rede_social/conteudos/agendados")
    for entry in result.entries:
        st.write("•", entry.name)
except Exception as e:
    st.warning("Nenhum arquivo encontrado ou pasta ainda não existe.")
