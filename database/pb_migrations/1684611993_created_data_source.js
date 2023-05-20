migrate((db) => {
  const collection = new Collection({
    "id": "js50r8yv2u12b4n",
    "created": "2023-05-20 19:46:33.858Z",
    "updated": "2023-05-20 19:46:33.858Z",
    "name": "data_source",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "vrvqwfr1",
        "name": "body",
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
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n");

  return dao.deleteCollection(collection);
})
