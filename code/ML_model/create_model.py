import mlflow.sklearn
import sklearn.datasets
import sklearn.tree

# create iris model
iris = sklearn.datasets.load_iris()
tree = sklearn.tree.DecisionTreeClassifier()
model = tree.fit(iris.data, iris.target)
tracking_uri = "/share/mlflow"
mlflow.set_tracking_uri(tracking_uri)
experiment_name = "base-iris"
mlflow.set_experiment(experiment_name)
mlflow.start_run()
accuracy = sum(model.predict(iris.data) == iris.target) / len(iris.target) 
mlflow.log_metrics({'accuracy': accuracy})
mlflow.sklearn.log_model(model, 'dicision_tree')
mlflow.end_run()


"""
# MLFLOW

### プロジェクト作成
`mlflow experiments create --experiment-name <プロジェクト名>`

### プロジェクトの設定ファイル作成
* ファイル名はconda.yamlと書くのがお約束みたい
  * models/cli.py serve でexec_cmdでcondaコマンドを叩くため

### 【途中放棄】MLFLOWのAPIを使う場合はanacondaを使わないとダメ!!
* pyenvをやめないとダメ？
* docker anaconda imageで再度試す

### 参考

* https://blog.imind.jp/entry/2019/06/14/232116


curl -d '{"columns":["x"], "data":[[1], [-1]]}' -H 'Content-Type: application/json; format=pandas-split' -X POST localhost:1234/invocations

curl -X POST \
    -H "Content-Type:application/json; format=pandas-records" \
    --data '{"0":{"0":5.1,"1":4.9,"2":4.7,"3":4.6,"4":5.0},"1":{"0":3.5,"1":3.0,"2":3.2,"3":3.1,"4":3.6},"2":{"0":1.4,"1":1.4,"2":1.3,"3":1.5,"4":1.4},"3":{"0":0.2,"1":0.2,"2":0.2,"3":0.2,"4":0.2}}' \
    http://localhost:1234/invocations

"""