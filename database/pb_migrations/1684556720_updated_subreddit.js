migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo")

  collection.listRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("uv8qpynh0k7f1uo")

  collection.listRule = null

  return dao.saveCollection(collection)
})
