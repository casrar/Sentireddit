migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  // remove
  collection.schema.removeField("fxnkvwnc")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

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
})
