
# Clean Script

Este é um script em Python que limpa o cache dos navegadores, remove arquivos temporários antigos e redefine as configurações de rede. Ele foi desenvolvido para ajudar na manutenção do sistema, removendo arquivos desnecessários e melhorando o desempenho.

## Funcionalidades

- **Limpeza de Cache de Navegadores**: Remove o cache dos navegadores mais comuns (Chrome, Firefox, Edge, Opera, Brave).
- **Remoção de Arquivos Temporários**: Apaga arquivos temporários do sistema com mais de 7 dias.
- **Redefinição de Configurações de Rede**: Faz o flush do cache DNS e renova o adaptador de rede.

## Pré-requisitos

- **Python 3.x**: Certifique-se de ter o Python 3 instalado para executar o script diretamente ou criar o executável.

## Como Usar

1. **Executar o Script**:
   - Você pode executar o script diretamente em Python ou utilizar o executável gerado.
   - O script solicitará confirmação antes de iniciar o processo de limpeza.

## Estrutura do Projeto

```
.
├── clean.py              # Script principal para limpeza de cache e redefinição de rede
├── README.md             # Documentação do projeto
└── clean.exe             # Executavel do script
```

## Como Funciona

Ao executar o script, ele segue os seguintes passos:

1. Exibe um aviso em ASCII e uma descrição das ações que serão realizadas.
2. Solicita confirmação do usuário para iniciar o processo.
3. Realiza a limpeza de cache dos navegadores suportados.
4. Remove arquivos temporários que não foram modificados nos últimos 7 dias.
5. Faz o flush do cache DNS e reinicia o adaptador de rede.

## Observações

- **Permissões de Administrador**: Para redefinir configurações de rede e remover certos arquivos temporários, o script pode precisar ser executado como administrador.
- **Compatibilidade**: Este script foi testado no Windows, mas pode ser adaptado para Linux e macOS com pequenas modificações.

## Contribuição

Sinta-se à vontade para fazer um fork do projeto e enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
