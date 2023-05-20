migrate((db) => {
  const collection = new Collection({
    "id": "uv8qpynh0k7f1uo",
    "created": "2023-05-20 03:23:12.352Z",
    "updated": "2023-05-20 03:23:12.352Z",
    "name": "data_source",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "ixypye4o",
        "name": "data_source_kvp",
        "type": "json",
        "required": false,
        "unique": false,
        "options": {}
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
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo");

  return dao.deleteCollection(collection);
})
