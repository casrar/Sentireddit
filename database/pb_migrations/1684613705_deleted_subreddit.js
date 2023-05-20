migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo");

  return dao.deleteCollection(collection);
}, (db) => {
  const collection = new Collection({
    "id": "uv8qpynh0k7f1uo",
    "created": "2023-05-20 03:23:12.352Z",
    "updated": "2023-05-20 04:25:20.624Z",
    "name": "subreddit",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "jbwb0dvo",
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
    "listRule": "",
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
})
