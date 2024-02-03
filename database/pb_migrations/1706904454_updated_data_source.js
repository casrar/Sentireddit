migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.viewRule = ""
  collection.updateRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.viewRule = null
  collection.updateRule = null

  return dao.saveCollection(collection)
})
