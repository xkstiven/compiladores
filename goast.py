# goast.py

    # --- nodos expressions ---
    def visit_UnaryOp(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Unary op\\noperator : %s",shape=box]\n'% node.op
        self.visit(node.left)
        left = self.st.pop()
        self.dot += '\t' + id_node + ' -> ' + left + '\n'
        self.st.append(id_node)

    def visit_BinaryOp(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Binary op\\noperator : %s",shape=box]\n'% node.op
        self.visit(node.left)
        self.visit(node.right)
        right = self.st.pop()
        left = self.st.pop()
        self.dot += '\t' + id_node + ' -> ' + left + '\n'
        self.dot += '\t' + id_node + ' -> ' + right + '\n'
        self.st.append(id_node)
        return

    def visit_RelationalOp(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Relational op\\noperator : %s",shape=box]\n'% node.op
        self.visit(node.left)
        self.visit(node.right)
        right = self.st.pop()
        left = self.st.pop()
        self.dot += '\t' + id_node + ' -> ' + left + '\n'
        self.dot += '\t' + id_node + ' -> ' + right + '\n'
        self.st.append(id_node)
        return

    def visit_Group(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Parenthesis",shape=box]\n'
        self.visit(node.expression)
        left = self.st.pop()
        self.dot += '\t' + id_node + ' -> ' + left + '\n'
        self.st.append(id_node)
        return

    def visit_LoadLocation(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Load location",shape=box]\n'
        self.visit(node.name)
        left = self.st.pop()
        self.dot += '\t' + id_node + ' -> ' + left + '\n'
        self.st.append(id_node)
        return

    def visit_ExprLiteral(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Expr literal",shape=box]\n'
        self.visit(node.value)
        left = self.st.pop()
        self.dot += '\t' + id_node + ' -> ' + left + '\n'
        self.st.append(id_node)
        return

    def visit_Expression_array(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Expr array",shape=box]\n'
        self.visit(node.name)
        self.visit(node.expression)
        right = self.st.pop()
        left = self.st.pop()
        self.dot += '\t' + id_node + ' -> ' + left + '\n'
        self.dot += '\t' + id_node + ' -> ' + right + '\n'
        self.st.append(id_node)
        return

    def visit_ExprList(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Parameters func call",shape=box]\n'
        # El for hace posible la visita nodo por nodo de una lista de nodos
        # donde cada nodo es una 'expression' qué coincide con algún parámetro de la función en llamada
        if node.expressions[0] != None: # Si la llamada a la función es con parámetros
            for param in node.expressions:
                self.visit(param)
                child_param = self.st.pop()
                self.dot += '\t' + id_node + ' -> ' + child_param + '\n'
        self.st.append(id_node)
        return
    # --- fin nodos expressions ---

    # --- nodos hojas ---
    def visit_Location(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Location\\nid : %s",shape=circle]\n'% node.id
        self.st.append(id_node)
        return

    def visit_Literal(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Literal\\nvalue : %s",shape=circle]\n'% node.value
        self.st.append(id_node)
        return

    def visit_ParamDecl(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Parameter\\nid : %s\\ntypename : %s",shape=circle]\n'% (node.id,node.typename)
        self.st.append(id_node)
        return

    def visit_SpecialLiteralArray(self,node):
        id_node = self.set_id_node()
        self.dot += '\t' + id_node + ' [label= "Literal array\\nReserved amount : %s",shape=circle]\n'% str(node.amount)
        self.st.append(id_node)
        return
    # --- fin nodos hojas ---
