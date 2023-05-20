migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo")

  // remove
  collection.schema.removeField("ixypye4o")

  // add
  collection.schema.addField(new SchemaField({
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
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ixypye4o",
    "name": "name",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  // remove
  collection.schema.removeField("jbwb0dvo")

  return dao.saveCollection(collection)
})
