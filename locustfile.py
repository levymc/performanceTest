from locust import HttpUser, task, between

class PerformanceTest(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZEVtcHJlc2EiOjE1NDksImF1dGhLZXkiOiJtZGItYXV0aC1rZXkiLCJpYXQiOjE3MDI0NzY0NDAsImV4cCI6MTcwMjQ3NzM0MCwic3ViIjoiNjJiM2Y5ZjYzOWI2YWQ3ZmYxYWZhYWRjIn0.Pgd9a5G9Gi6QghiH69BnKzsnWExJFdZjWeB8o6UPWQ4'
        # self.client.cookies.set('JSESSIONID', '38D47E85BC20CC14FAB5CF600C93DBFC')

    @task
    def getPage(self):
        # Adicione o token Bearer ao cabeçalho de autorização
        headers = {
            'Authorization': f'Bearer {self.token}',
            'idEmpresa': '1549'
        }

        params = {
            'parametro1': 'valor1',
            'parametro2': 'valor2'
        }

        response = self.client.get(
            # "WeHandle.jsp?url=logado/ajax/validacao_filtros.jsp?ajax=true&unidadeTerceiro=%5B%221966%22%5D&pessoaTerceiro=%5B%5D&documentos=%5B%5D&emvalidacaoFiltro=false&validadosFiltro=false&empresaFiltro=false&funcionariosFiltro=false&historico=true&dataLimite=",
            "integrations/nwaypro/users",
            headers=headers,
            # params=params
        )
        print(response)
        if response.status_code == 200:
            print("Requisição bem-sucedida!")
        else:
            print(f"Falha na requisição. Código de status: {response.status_code}")
