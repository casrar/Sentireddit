migrate((db) => {
  const collection = new Collection({
    "id": "ktatp8abyt8ji5o",
    "created": "2024-02-02 19:30:31.202Z",
    "updated": "2024-02-02 19:30:31.202Z",
    "name": "scraper_delay",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "ppn6cgce",
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
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("ktatp8abyt8ji5o");

  return dao.deleteCollection(collection);
})
