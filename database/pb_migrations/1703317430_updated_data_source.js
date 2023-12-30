migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "q4nsec9f",
    "name": "query",
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
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "q4nsec9f",
    "name": "search_term",
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
})
