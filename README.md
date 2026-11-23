# Serverless Order API

Det här är mitt projekt i kursen Serverless-utveckling (20 YHP). Jag har byggt ett enkelt API för att skapa, hämta och uppdatera beställningar.

Jag använder tre AWS-tjänster:
- **API Gateway** tar emot anrop från Postman.
- **Lambda** kör Python-koden.
- **DynamoDB** sparar beställningarna i tabellen `table1`.

## Mina tre funktioner

| Metod | Route | Lambda | Vad den gör |
| --- | --- | --- | --- |
| POST | `/orders` | `post-func` | Skapar en ny order |
| GET | `/orders/{id}` | `get-func` | Hämtar en order |
| PUT | `/orders/{id}` | `put-fuc` | Ändrar orderns status |

Tabellen heter `table1`, och `partikey` är partition key (String). Varje order får ett eget ID.

## Så testade jag

Jag använde Postman och testade i den här ordningen:

1. **POST /orders** med `{"product":"Trimmer"}` – skapar en order med status `new`.
2. **GET /orders/{id}** – hämtar ordern med det ID jag fick från POST.
3. **PUT /orders/{id}** med `{"status":"shipped"}` – uppdaterar ordern.
4. **GET /orders/{id}** igen – kontrollerar att statusen har sparats som `shipped`.

API:et körs i AWS-regionen **eu-north-1 (Stockholm)**. Jag använder Python och `boto3` för att prata med DynamoDB.

## Filerna

Varje mapp innehåller koden för motsvarande Lambda-funktion. I AWS har de handler `lambda_function.lambda_handler`.

Det här repot är för kodinlämningen. Själva API:et är driftsatt i AWS. Om jag ändrar koden i AWS behöver jag uppdatera filerna här också.
