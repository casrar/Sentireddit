migrate((db) => {
  const collection = new Collection({
    "id": "1v6d2tdwyh005gp",
    "created": "2024-01-28 02:57:58.134Z",
    "updated": "2024-01-28 02:57:58.134Z",
    "name": "scraping_schedule",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "hchho5hx",
        "name": "scraper_delay",
        "type": "number",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": "",
    "createRule": null,
    "updateRule": "",
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("1v6d2tdwyh005gp");

  return dao.deleteCollection(collection);
})
