migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.listRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("js50r8yv2u12b4n")

  collection.listRule = null

  return dao.saveCollection(collection)
})
