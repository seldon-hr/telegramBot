import logging
from notion_client import Client

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Establecer logging
logging.basicConfig(
    format='%(asctime)s -%(name)s %(levelname)s -%(message)s',
    level=logging.INFO    
)
logger = logging.getLogger(__name__)


# Creenciales
NOTION_TOKEN = open('notion_integration_token.txt').read().strip()
NOTION_DB_ID = open('notion_database_id.txt').read().strip()
TELEGRAM_TOKEN = open('telegram_bot_token.txt').read().strip()

# Initialize API clients
notion = Client(auth=NOTION_TOKEN)



# Recibir mensaje del chat
def receive_buyment():
    logger.debug("Mensaje recibido")
    

async def send_grettng(update: Update):
    await update.message.reply_text('Hola, estas interactuando con un bot con conexión a Notion :)')

def connecting_notion_db() -> None:
    db_info = notion.databases.retrieve(database_id=NOTION_DB_ID)
    title = db_info['title'][0]['text']['content']
    logger.info(f"Conectado a la db: {title}")



# Main funtion
def main() -> None:
    """ Conectar con Notion DB"""
    connecting_notion_db()

    """Conectar y levantar la aplicación del bot"""
    # Creación de la app como instancia del constructor y aprobación por medio del token del bot.
    telegram_app_bot = Application.builder().token(TELEGRAM_TOKEN).build()

    # Controller respectivo para ruta de /hola en el bot
    telegram_app_bot.add_handler(CommandHandler("hola",send_grettng))

    # Petición que el server le va a estar preguntando constantemente a telegram si hay, un polling.
    telegram_app_bot.run_polling()





if __name__ == "__main__":
    main()