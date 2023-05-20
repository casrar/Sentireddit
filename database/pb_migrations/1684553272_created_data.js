migrate((db) => {
  const collection = new Collection({
    "id": "9lgohp90l2nt12k",
    "created": "2023-05-20 03:27:52.037Z",
    "updated": "2023-05-20 03:27:52.037Z",
    "name": "data",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "apncng3b",
        "name": "body",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "vi4lq7eq",
        "name": "post_id",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "ymv9x7dl",
        "name": "search_term",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "tx7oy5ef",
        "name": "post_date",
        "type": "date",
        "required": false,
        "unique": false,
        "options": {
          "min": "",
          "max": ""
        }
      },
      {
        "system": false,
        "id": "9yzrwz7f",
        "name": "sentiment",
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
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k");

  return dao.deleteCollection(collection);
})
