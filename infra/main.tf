resource "kubernetes_namespace" "devops" {
  metadata {
    name = "devops"
  }
}
# Deployment

resource "kubernetes_deployment" "quiz_app" {
  metadata {
    name      = "quiz-app"
    namespace = kubernetes_namespace.devops.metadata[0].name
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "quiz-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "quiz-app"
        }
      }

      spec {
        container {
          image = "tehseen45/devops_quiz_app:latest" 
          name  = "quiz-app-container"

          port {
            container_port = 8000
          }
        }
      }
    }
  }
}




resource "kubernetes_service" "quiz_service" {
  metadata {
    name      = "quiz-service"
    namespace = kubernetes_namespace.devops.metadata[0].name
  }

  spec {
    selector = {
      app = kubernetes_deployment.quiz_app.spec[0].template[0].metadata[0].labels.app
    }

    port {
      port        = 80
      target_port = 8000
    }

    type = "NodePort"
  }
}
