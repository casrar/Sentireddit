migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  // remove
  collection.schema.removeField("kuhfudtj")

  // remove
  collection.schema.removeField("9yzrwz7f")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "uqigelfl",
    "name": "post_date",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "4fjtjw2q",
    "name": "sentiment",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "kuhfudtj",
    "name": "post_date",
    "type": "number",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "9yzrwz7f",
    "name": "sentiment",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  // remove
  collection.schema.removeField("uqigelfl")

  // remove
  collection.schema.removeField("4fjtjw2q")

  return dao.saveCollection(collection)
})
