migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  // remove
  collection.schema.removeField("8tx2ssre")

  // remove
  collection.schema.removeField("ymv9x7dl")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "nvrh3m9w",
    "name": "data_source",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "js50r8yv2u12b4n",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("9lgohp90l2nt12k")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "8tx2ssre",
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
  }))

  // remove
  collection.schema.removeField("nvrh3m9w")

  return dao.saveCollection(collection)
})
