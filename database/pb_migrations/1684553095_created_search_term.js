migrate((db) => {
  const collection = new Collection({
    "id": "nufb9h5u2fx6kh6",
    "created": "2023-05-20 03:24:55.813Z",
    "updated": "2023-05-20 03:24:55.813Z",
    "name": "search_term",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "2lrblewe",
        "name": "name",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
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
  const collection = dao.findCollectionByNameOrId("nufb9h5u2fx6kh6");

  return dao.deleteCollection(collection);
})
