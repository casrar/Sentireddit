migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo")

  collection.name = "subreddit"

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ixypye4o",
    "name": "name",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo")

  collection.name = "data_source"

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ixypye4o",
    "name": "data_source_kvp",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  return dao.saveCollection(collection)
})
