migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  // remove
  collection.schema.removeField("vrvqwfr1")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "vrumydke",
    "name": "subreddit",
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
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "vrvqwfr1",
    "name": "body",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  // remove
  collection.schema.removeField("vrumydke")

  // remove
  collection.schema.removeField("q4nsec9f")

  return dao.saveCollection(collection)
})
