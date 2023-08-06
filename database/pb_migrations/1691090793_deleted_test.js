migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("z2ahh9x8gwe6af7");

  return dao.deleteCollection(collection);
}, (db) => {
  const collection = new Collection({
    "id": "z2ahh9x8gwe6af7",
    "created": "2023-08-03 19:24:09.050Z",
    "updated": "2023-08-03 19:24:09.050Z",
    "name": "test",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "b5gkfngy",
        "name": "data_source",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "js50r8yv2u12b4n",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": []
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
})
