migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  // remove
  collection.schema.removeField("uqigelfl")

  // remove
  collection.schema.removeField("4fjtjw2q")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "qiuoegor",
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
    "id": "fxnkvwnc",
    "name": "sentiment",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

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

  // remove
  collection.schema.removeField("qiuoegor")

  // remove
  collection.schema.removeField("fxnkvwnc")

  return dao.saveCollection(collection)
})
