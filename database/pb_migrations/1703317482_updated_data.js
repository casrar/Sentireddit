migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "qin1gghc",
    "name": "post_id",
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

  // remove
  collection.schema.removeField("qin1gghc")

  return dao.saveCollection(collection)
})
