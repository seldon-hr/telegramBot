import logging
from notion_client import Client

# Establecer logging
logging.basicConfig(
    format='%(asctime)s -%(name)s %(levelname)s -%(message)s',
    level=logging.INFO    
)
logger = logging.getLogger(__name__)


# Creenciales
NOTION_TOKEN = open('notion_integration_token.txt').read().strip()
NOTION_DB_ID = open('notion_database_id.txt').read().strip()

# Initialize Notion client
notion = Client(auth=NOTION_TOKEN)


# Main funtion
def main() -> None:
    logger.info(f"Nos devuelve var {notion}")
    db_info = notion.databases.retrieve(database_id=NOTION_DB_ID)
    logger.info(f"DB de notion list {db_info}")




if __name__ == "__main__":
    main()