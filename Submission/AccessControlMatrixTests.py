import ReferenceMonitor

def testNoRole():
    print('Running No Role tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('')
    writePermissions = monitor.assignWritePermission('')
    assert(readPermissions == [])
    assert(writePermissions == [])
    print('Passing No Role tests\n')

def testInvalidRole():
    print('Running Invalid Role tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Invalid')
    writePermissions = monitor.assignWritePermission('Invalid')
    assert(readPermissions == [])
    assert(writePermissions == [])
    print('Passing Invalid Role tests\n')

def testClient():
    print('Running Client tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Client')
    writePermissions = monitor.assignWritePermission('Client')
    assert(readPermissions == ['Account balance', 'Investment portfolio', 'FA contact details'])
    assert(writePermissions == [])
    print('Passing Client tests\n')

def testPremiumClient():
    print('Running Premium Client tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Premium Client')
    writePermissions = monitor.assignWritePermission('Premium Client')
    assert(readPermissions == ['Account balance', 'Investment portfolio', 'FI contact details', 'FP contact details'])
    assert(writePermissions == ['Investment portfolio'])
    print('Passing Premium Client tests\n')

def testFinancialPlanner():
    print('Running Financial Planner tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Financial Planner')
    writePermissions = monitor.assignWritePermission('Financial Planner')
    assert(readPermissions == ['Clients account balance', 'Clients investment portfolio', 'Money market instruments', 'Private consumer instruments'])
    assert(writePermissions == ['Clients account balance', 'Clients investment portfolio'])
    print('Passing Financial Planner tests\n')

def testFinancialAdvisor():
    print('Running Financial Advisor tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Financial Advisor')
    writePermissions = monitor.assignWritePermission('Financial Advisor')
    assert(readPermissions == ['Clients account balance', 'Clients investment portfolio', 'Private consumer instruments'])
    assert(writePermissions == ['Clients account balance', 'Clients investment portfolio'])
    print('Passing Financial Advisor tests\n')

def testInvestmentAnalyst():
    print('Running Investment Analyst tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Investment Analyst')
    writePermissions = monitor.assignWritePermission('Investment Analyst')
    assert(readPermissions == ['Clients account balance', 'Clients investment portfolio', 'Money market instruments',
                               'Derivatives trading', 'Interest instruments', 'Clients account access',
                               'Validate investment portfolio modifications'])
    assert(writePermissions == ['Clients account balance', 'Clients investment portfolio'])
    print('Passing Investment Analyst tests\n')
    
def testTechnicalSupport():
    print('Running Technical Support tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Technical Support')
    writePermissions = monitor.assignWritePermission('Technical Support')
    assert(readPermissions == ['Clients account balance', 'Clients investment portfolio', 'Clients account access',
                               'Validate investment portfolio modifications'])
    assert(writePermissions == ['Clients account access', 'Validate investment portfolio modifications'])
    print('Passing Technical Support tests\n')

def testTeller():
    print('Running Teller tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Teller')
    writePermissions = monitor.assignWritePermission('Teller')
    assert(readPermissions == ['Clients account balance', 'Clients investment portfolio'])
    assert(writePermissions == [])
    print('Passing Teller tests\n')

def testComplianceOfficer():
    print('Running Compliance Officer tests')
    monitor = ReferenceMonitor.ReferenceMonitor()
    readPermissions = monitor.assignReadPermission('Compliance Officer')
    writePermissions = monitor.assignWritePermission('Compliance Officer')
    assert(readPermissions == ['Clients account balance', 'Clients investment portfolio', 'Validate investment portfolio modifications'])
    assert(writePermissions == [])
    print('Passing Compliance Officer tests\n')

def runTests():
    print('\n-------------------------')
    print('----- RUNNING TESTS -----')
    print('- Access Control Matrix -')
    print('-------------------------')
    testNoRole()
    testInvalidRole()
    testClient()
    testPremiumClient()
    testFinancialPlanner()
    testFinancialAdvisor()
    testInvestmentAnalyst()
    testTechnicalSupport()
    testTeller()
    testComplianceOfficer()
    print('-------------------------')
    print('----- ALL TESTS PASS ----')
    print('-------------------------')

runTests()