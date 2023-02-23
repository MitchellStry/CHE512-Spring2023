def taylor1(taylor_aporx,exact):
        """"
            This function should compute 1/(1-x) using taylor series epansions
                1/(1-x) \aprox 1+x+x^2+x^3...
                    conditions 0<x<1
                        returns:
                            tuple:taylor_apporx, exact result
                                """
                                    x=taylor_aporx
                                        N=exact
                                            taylor,exact=0.0,1.0/(1-x)
                                                n=0
                                                    x1=0
                                                        while n<N:
                                                                    x1=x1+(x**n)
                                                                            n+=1
                                                                                taylor=x1
                                                                                    return taylor, exact

                                                                                print(taylor1(0.99,1000))
